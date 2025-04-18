def assess_recurrence_risk(fraction_genome_altered, therapy_type=None):
    """
    Assess risk of recurrence based on SCNA burden (Fraction Genome Altered).
    """
    if fraction_genome_altered > 0.3:
        return "High Risk"
    elif fraction_genome_altered > 0.2:
        return "Moderate Risk"
    else:
        return "Low Risk"
