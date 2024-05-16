import sys
import json


def fill(struct):
    global valuesDict
    if 'values' in struct:
        if struct['id'] in valuesDict:
            struct['value'] = valuesDict[struct['id']]
        for value in struct['values']:
            fill(value)
    else:
        if struct['id'] in valuesDict:
            struct['value'] = valuesDict[struct['id']]


if __name__ == '__main__':
    _, valuesPath, testsPath, reportPath = sys.argv

    with open(valuesPath, 'r') as valuesFile:
        valuesJson = json.load(valuesFile)
    with open(testsPath, 'r') as testsFile:
        testsJson = json.load(testsFile)

    valuesDict = {test['id']: test['value'] for test in valuesJson['values']}

    for test in testsJson['tests']:
        fill(test)

    with open(reportPath, 'w') as reportFile:
        json.dump(testsJson, reportFile, indent=2, )
