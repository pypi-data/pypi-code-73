# pylint: disable:invalid-name
"""
This file contains constant definitions.
"""

# MEASUREMENTS

OBSERVABLE_ID = 'observableId'
PREEQUILIBRATION_CONDITION_ID = 'preequilibrationConditionId'
SIMULATION_CONDITION_ID = 'simulationConditionId'
MEASUREMENT = 'measurement'
TIME = 'time'
OBSERVABLE_PARAMETERS = 'observableParameters'
NOISE_PARAMETERS = 'noiseParameters'
DATASET_ID = 'datasetId'
REPLICATE_ID = 'replicateId'

MEASUREMENT_DF_REQUIRED_COLS = [
    OBSERVABLE_ID, SIMULATION_CONDITION_ID, MEASUREMENT, TIME]

MEASUREMENT_DF_OPTIONAL_COLS = [
    PREEQUILIBRATION_CONDITION_ID, OBSERVABLE_PARAMETERS,
    NOISE_PARAMETERS,
    DATASET_ID, REPLICATE_ID]

MEASUREMENT_DF_COLS = [
    MEASUREMENT_DF_REQUIRED_COLS[0], MEASUREMENT_DF_OPTIONAL_COLS[0],
    *MEASUREMENT_DF_REQUIRED_COLS[1:], *MEASUREMENT_DF_OPTIONAL_COLS[1:]]


# PARAMETERS

PARAMETER_ID = 'parameterId'
PARAMETER_NAME = 'parameterName'
PARAMETER_SCALE = 'parameterScale'
LOWER_BOUND = 'lowerBound'
UPPER_BOUND = 'upperBound'
NOMINAL_VALUE = 'nominalValue'
ESTIMATE = 'estimate'
INITIALIZATION_PRIOR_TYPE = 'initializationPriorType'
INITIALIZATION_PRIOR_PARAMETERS = 'initializationPriorParameters'
OBJECTIVE_PRIOR_TYPE = 'objectivePriorType'
OBJECTIVE_PRIOR_PARAMETERS = 'objectivePriorParameters'

PARAMETER_DF_REQUIRED_COLS = [
    PARAMETER_ID, PARAMETER_SCALE, LOWER_BOUND, UPPER_BOUND, ESTIMATE]

PARAMETER_DF_OPTIONAL_COLS = [
    PARAMETER_NAME, NOMINAL_VALUE,
    INITIALIZATION_PRIOR_TYPE, INITIALIZATION_PRIOR_PARAMETERS,
    OBJECTIVE_PRIOR_TYPE, OBJECTIVE_PRIOR_PARAMETERS]

PARAMETER_DF_COLS = [
    PARAMETER_DF_REQUIRED_COLS[0], PARAMETER_DF_OPTIONAL_COLS[0],
    *PARAMETER_DF_REQUIRED_COLS[1:], *PARAMETER_DF_OPTIONAL_COLS[1:]]

INITIALIZATION = 'initialization'
OBJECTIVE = 'objective'


# CONDITIONS

CONDITION_ID = 'conditionId'
CONDITION_NAME = 'conditionName'


# OBSERVABLES

OBSERVABLE_NAME = 'observableName'
OBSERVABLE_FORMULA = 'observableFormula'
NOISE_FORMULA = 'noiseFormula'
OBSERVABLE_TRANSFORMATION = 'observableTransformation'
NOISE_DISTRIBUTION = 'noiseDistribution'

OBSERVABLE_DF_REQUIRED_COLS = [
    OBSERVABLE_ID, OBSERVABLE_FORMULA, NOISE_FORMULA]

OBSERVABLE_DF_OPTIONAL_COLS = [
    OBSERVABLE_NAME, OBSERVABLE_TRANSFORMATION, NOISE_DISTRIBUTION]

OBSERVABLE_DF_COLS = [
    *OBSERVABLE_DF_REQUIRED_COLS, *OBSERVABLE_DF_OPTIONAL_COLS]


# TRANSFORMATIONS

LIN = 'lin'
LOG = 'log'
LOG10 = 'log10'
OBSERVABLE_TRANSFORMATIONS = [LIN, LOG, LOG10]


# NOISE MODELS

UNIFORM = 'uniform'
PARAMETER_SCALE_UNIFORM = 'parameterScaleUniform'
NORMAL = 'normal'
PARAMETER_SCALE_NORMAL = 'parameterScaleNormal'
LAPLACE = 'laplace'
PARAMETER_SCALE_LAPLACE = 'parameterScaleLaplace'
LOG_NORMAL = 'logNormal'
LOG_LAPLACE = 'logLaplace'

PRIOR_TYPES = [
    UNIFORM, NORMAL, LAPLACE, LOG_NORMAL, LOG_LAPLACE,
    PARAMETER_SCALE_UNIFORM, PARAMETER_SCALE_NORMAL, PARAMETER_SCALE_LAPLACE]

NOISE_MODELS = [NORMAL, LAPLACE]


# VISUALIZATION

PLOT_ID = 'plotId'
PLOT_NAME = 'plotName'
PLOT_TYPE_SIMULATION = 'plotTypeSimulation'
PLOT_TYPE_DATA = 'plotTypeData'
X_VALUES = 'xValues'
X_OFFSET = 'xOffset'
X_LABEL = 'xLabel'
X_SCALE = 'xScale'
Y_VALUES = 'yValues'
Y_OFFSET = 'yOffset'
Y_LABEL = 'yLabel'
Y_SCALE = 'yScale'
LEGEND_ENTRY = 'legendEntry'

LINE_PLOT = 'LinePlot'
BAR_PLOT = 'BarPlot'
SCATTER_PLOT = 'ScatterPlot'
PLOT_TYPES_SIMULATION = [LINE_PLOT, BAR_PLOT, SCATTER_PLOT]


MEAN_AND_SD = 'MeanAndSD'
MEAN_AND_SEM = 'MeanAndSEM'
REPLICATE = 'replicate'
PROVIDED = 'provided'
PLOT_TYPES_DATA = [MEAN_AND_SD, MEAN_AND_SEM, REPLICATE, PROVIDED]


# YAML
FORMAT_VERSION = 'format_version'
PARAMETER_FILE = 'parameter_file'
PROBLEMS = 'problems'
SBML_FILES = 'sbml_files'
CONDITION_FILES = 'condition_files'
MEASUREMENT_FILES = 'measurement_files'
OBSERVABLE_FILES = 'observable_files'
VISUALIZATION_FILES = 'visualization_files'


# MORE

SIMULATION = 'simulation'
RESIDUAL = 'residual'
NOISE_VALUE = 'noiseValue'
