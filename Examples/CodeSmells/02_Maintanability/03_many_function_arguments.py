# Code smell
def start_measurement_set(self, measurement_set_name: str, max_drift_sample_sage: float =-1,
                          target_cs: CS = CS.ACP, drift_option: DriftOption = DriftOption.DRIFT_PRE_CONV,
                          post_drift_sample_delay: float = None, log_vcm: bool = False,
                          log_init_sensor: bool = False):

# Better
def start_measurement_set(self, settings: MeasurementSettings):
    """
    Starts a Measurement set:
    ...
    """

if __name__ == '__main__':
    pass