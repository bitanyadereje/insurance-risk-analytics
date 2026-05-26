def run_ttest(a,b):
    from scipy import stats
    return stats.ttest_ind(a,b)
