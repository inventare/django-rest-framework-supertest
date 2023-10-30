from ._utils import unique


def job_name(fake: object) -> str:
    """Generate a job name."""
    return fake.job()

def unique_job_name(fake: object) -> str:
    """Generate a unique job name."""
    return unique(fake, job_name)
