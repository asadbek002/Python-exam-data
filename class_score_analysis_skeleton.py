import csv
from statistics import mean, variance, median

def read_data(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if not row or row[0].startswith('#'):
                    continue
                data.append([int(item) for item in row])
    except FileNotFoundError:
        print(f"File not found: {filename}")
    return data

def calc_weighted_average(data_2d, weights):
    # TODO: Calculate the weighted averages of each row of `data_2d`
    averages = []
    for row in data_2d:
        weighted_avg = sum(val * weight for val, weight in zip(row, weights))
        averages.append(weighted_avg)
    return averages

def analyze_data(data_1d):
    # TODO: Derive summary statistics of the given `data_1d`
    mean_val = mean(data_1d)
    variance_val = variance(data_1d)
    median_val = median(data_1d)
    min_val = min(data_1d)
    max_val = max(data_1d)
    return mean_val, variance_val, median_val, min_val, max_val

# Example usage
if __name__ == '__main__':
    data = read_data('data/class_score_en.csv')
    
    if data and len(data[0]) == 2:  # Check if 'data' is valid
        weights = [40 / 125, 60 / 100]  # Sample weights

        # Calculate weighted averages
        average = calc_weighted_average(data, weights)

        # Write the analysis report as a markdown file
        with open('class_score_analysis.md', 'w') as report:
            report.write('### Individual Score\n\n')
            report.write('| Midterm | Final | Total |\n')
            report.write('| ------- | ----- | ----- |\n')
            for ((m_score, f_score), a_score) in zip(data, average):
                report.write(f'| {m_score} | {f_score} | {a_score:.3f} |\n')
            report.write('\n\n\n')

            report.write('### Examination Analysis\n')
            data_columns = {
                'Midterm': [m_score for m_score, _ in data],
                'Final': [f_score for _, f_score in data],
                'Average': average
            }
            for name, column in data_columns.items():
                mean_val, variance_val, median_val, min_val, max_val = analyze_data(column)
                report.write(f'* {name}\n')
                report.write(f'  * Mean: **{mean_val:.3f}**\n')
                report.write(f'  * Variance: {variance_val:.3f}\n')
                report.write(f'  * Median: **{median_val:.3f}**\n')
                report.write(f'  * Min/Max: ({min_val:.3f}, {max_val:.3f})\n')
