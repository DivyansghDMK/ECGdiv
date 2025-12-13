#!/usr/bin/env python3
import re
import sys

# Read ADC data from stdin or file
adc_lines = []
for line in sys.stdin:
    line = line.strip()
    if line and not line.startswith('$') and not line.startswith('----'):
        # Extract all numbers from the line
        numbers = re.findall(r'\d+', line)
        if len(numbers) >= 8:  # At least 8 columns
            adc_lines.append([int(n) for n in numbers[:8]])

# Initialize leads (assuming 8 columns: I, II, III, aVR, aVL, aVF, V1, V2)
leads_max = {
    'I': [],
    'II': [],
    'III': [],
    'aVR': [],
    'aVL': [],
    'aVF': [],
    'V1': [],
    'V2': []
}

# Collect all values for each lead
for row in adc_lines:
    if len(row) >= 8:
        leads_max['I'].append(row[0])
        leads_max['II'].append(row[1])
        leads_max['III'].append(row[2])
        leads_max['aVR'].append(row[3])
        leads_max['aVL'].append(row[4])
        leads_max['aVF'].append(row[5])
        leads_max['V1'].append(row[6])
        leads_max['V2'].append(row[7])

# Find maximum for each lead
baseline = 2000.0
wave_gain = 10.0
adc_per_box = 7500.0 / wave_gain

print("=" * 70)
print("HIGHEST ADC VALUES FROM SERIAL PORT DATA")
print("=" * 70)
print()
print(f"{'Lead':<8} {'Highest ADC':<15} {'After Baseline':<15} {'Boxes':<15}")
print("-" * 70)

for lead in ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2']:
    if leads_max[lead]:
        highest = max(leads_max[lead])
        after_baseline = highest - baseline
        boxes = after_baseline / adc_per_box
        print(f"{lead:<8} {highest:<15.1f} {after_baseline:<15.1f} {boxes:<15.3f}")

print()
print("=" * 70)
print("CALCULATION VERIFICATION:")
print("=" * 70)
print()
print(f"Baseline: {baseline}")
print(f"Wave gain: {wave_gain} mm/mV")
print(f"ADC per box: {adc_per_box:.2f}")
print()
print("Formula: boxes = (highest_adc - baseline) / adc_per_box")
print(f"         boxes = (highest_adc - {baseline}) / {adc_per_box:.2f}")

