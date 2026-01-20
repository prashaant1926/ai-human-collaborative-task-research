"""
Analysis Template for Human-AI Collaboration Experiments
=========================================================

This script provides reusable analysis functions for the experiment data.
Adapt as needed for specific analyses.
"""

import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.anova import AnovaRM
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)


def load_interaction_logs(filepath):
    """Load and preprocess interaction log data."""
    df = pd.read_json(filepath, lines=True)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df


def load_survey_data(filepath):
    """Load and preprocess survey responses."""
    df = pd.read_csv(filepath)
    return df


def calculate_nasa_tlx_scores(df, weighted=True):
    """
    Calculate NASA-TLX composite scores.

    Parameters:
    -----------
    df : DataFrame with NASA-TLX subscale columns
    weighted : bool, whether to apply importance weights

    Returns:
    --------
    Series of composite scores
    """
    subscales = ['mental_demand', 'physical_demand', 'temporal_demand',
                 'performance', 'effort', 'frustration']

    if weighted:
        # Would need weight columns from pairwise comparisons
        # For now, use unweighted (Raw TLX)
        pass

    return df[subscales].mean(axis=1)


def run_repeated_measures_anova(df, dv, subject, within):
    """
    Run repeated measures ANOVA.

    Parameters:
    -----------
    df : DataFrame in long format
    dv : str, dependent variable column name
    subject : str, subject identifier column
    within : str or list, within-subject factor(s)

    Returns:
    --------
    ANOVA results table
    """
    aovrm = AnovaRM(df, dv, subject, within=[within] if isinstance(within, str) else within)
    results = aovrm.fit()
    return results


def calculate_effect_size_eta_squared(ss_effect, ss_total):
    """Calculate partial eta-squared effect size."""
    return ss_effect / ss_total


def plot_condition_comparison(df, dv, condition_col='condition',
                              title='Comparison by Condition'):
    """
    Create box plot comparing conditions.

    Parameters:
    -----------
    df : DataFrame
    dv : str, dependent variable to plot
    condition_col : str, column with condition labels
    title : str, plot title
    """
    fig, ax = plt.subplots()

    # Box plot with individual points
    sns.boxplot(x=condition_col, y=dv, data=df, ax=ax, palette='Set2')
    sns.stripplot(x=condition_col, y=dv, data=df, ax=ax,
                  color='black', alpha=0.5, jitter=True)

    ax.set_title(title)
    ax.set_xlabel('Condition')
    ax.set_ylabel(dv.replace('_', ' ').title())

    plt.tight_layout()
    return fig


def plot_learning_curves(df, x='session', y='completion_time',
                         hue='condition', title='Learning Curves'):
    """
    Plot learning curves across sessions by condition.

    Parameters:
    -----------
    df : DataFrame
    x : str, x-axis variable (typically session number)
    y : str, y-axis variable (outcome measure)
    hue : str, grouping variable (condition)
    title : str, plot title
    """
    fig, ax = plt.subplots()

    sns.lineplot(x=x, y=y, hue=hue, data=df, ax=ax,
                 marker='o', err_style='band', ci=95)

    ax.set_title(title)
    ax.set_xlabel('Session')
    ax.set_ylabel(y.replace('_', ' ').title())

    plt.tight_layout()
    return fig


def plot_nasa_tlx_radar(means_dict, title='NASA-TLX Profile by Condition'):
    """
    Create radar chart of NASA-TLX subscales.

    Parameters:
    -----------
    means_dict : dict, {condition: {subscale: mean}}
    title : str, plot title
    """
    subscales = ['Mental Demand', 'Physical Demand', 'Temporal Demand',
                 'Performance', 'Effort', 'Frustration']

    # Number of variables
    N = len(subscales)

    # Compute angle for each axis
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]  # Complete the loop

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    colors = plt.cm.Set2.colors

    for i, (condition, values) in enumerate(means_dict.items()):
        vals = [values.get(s.lower().replace(' ', '_'), 0) for s in subscales]
        vals += vals[:1]  # Complete the loop

        ax.plot(angles, vals, 'o-', linewidth=2, label=condition, color=colors[i])
        ax.fill(angles, vals, alpha=0.25, color=colors[i])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(subscales)
    ax.set_title(title)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))

    plt.tight_layout()
    return fig


def run_pairwise_comparisons(df, dv, group_col, method='tukey'):
    """
    Run post-hoc pairwise comparisons.

    Parameters:
    -----------
    df : DataFrame
    dv : str, dependent variable
    group_col : str, grouping variable
    method : str, 'tukey' or 'bonferroni'

    Returns:
    --------
    Comparison results
    """
    from statsmodels.stats.multicomp import pairwise_tukeyhsd

    if method == 'tukey':
        tukey = pairwise_tukeyhsd(df[dv], df[group_col])
        return tukey
    else:
        # Implement bonferroni if needed
        raise NotImplementedError("Only Tukey HSD currently implemented")


def calculate_icc(ratings_df, raters_col='rater', items_col='item', score_col='score'):
    """
    Calculate Intraclass Correlation Coefficient for inter-rater reliability.

    Parameters:
    -----------
    ratings_df : DataFrame with columns for rater, item, and score

    Returns:
    --------
    ICC value and interpretation
    """
    # Pivot to wide format
    wide = ratings_df.pivot(index=items_col, columns=raters_col, values=score_col)

    # Calculate ICC using ANOVA approach (ICC(2,k))
    n_items = len(wide)
    n_raters = len(wide.columns)

    # Grand mean
    grand_mean = wide.values.mean()

    # Between-items variance
    item_means = wide.mean(axis=1)
    ss_items = n_raters * ((item_means - grand_mean) ** 2).sum()

    # Between-raters variance
    rater_means = wide.mean(axis=0)
    ss_raters = n_items * ((rater_means - grand_mean) ** 2).sum()

    # Residual variance
    ss_total = ((wide.values - grand_mean) ** 2).sum()
    ss_residual = ss_total - ss_items - ss_raters

    # Mean squares
    ms_items = ss_items / (n_items - 1)
    ms_raters = ss_raters / (n_raters - 1)
    ms_residual = ss_residual / ((n_items - 1) * (n_raters - 1))

    # ICC(2,k) - average of k raters, random raters
    icc = (ms_items - ms_residual) / (ms_items + (ms_raters - ms_residual) / n_items)

    # Interpretation
    if icc < 0.5:
        interpretation = "Poor"
    elif icc < 0.75:
        interpretation = "Moderate"
    elif icc < 0.9:
        interpretation = "Good"
    else:
        interpretation = "Excellent"

    return icc, interpretation


# Example usage (when data is available)
if __name__ == "__main__":
    print("Analysis template loaded.")
    print("Functions available:")
    print("  - load_interaction_logs()")
    print("  - load_survey_data()")
    print("  - calculate_nasa_tlx_scores()")
    print("  - run_repeated_measures_anova()")
    print("  - plot_condition_comparison()")
    print("  - plot_learning_curves()")
    print("  - plot_nasa_tlx_radar()")
    print("  - run_pairwise_comparisons()")
    print("  - calculate_icc()")
