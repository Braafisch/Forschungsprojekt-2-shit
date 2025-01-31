import numpy as np
import struct
import os

def generate_fake_radar_data(file_size_mb, num_receivers=4, num_transmitters=3, sampling_rate_msps=25, if_bandwidth_mhz=10, output_file="radar_data.bin"):
    """
    Generates fake radar ADC data and saves it to a file based on the desired file size.

    Parameters:
    file_size_mb (int): Desired file size in megabytes.
    num_receivers (int): Number of receivers.
    num_transmitters (int): Number of transmitters.
    sampling_rate_msps (int): Sampling rate in MSPS (Mega Samples Per Second).
    if_bandwidth_mhz (int): IF bandwidth in MHz.
    output_file (str): Name of the file to save the data.
    """
    # Calculate the number of samples needed to achieve the desired file size
    sample_size_bytes = num_receivers * num_transmitters * 2  # 2 bytes per sample (uint16)
    total_samples = (file_size_mb * 1024 * 1024) // sample_size_bytes

    print(f"Generating {total_samples} samples of radar ADC data for {num_receivers} receivers and {num_transmitters} transmitters.")

    # Generate random radar ADC data
    data = np.random.randint(0, 4096, (total_samples, num_receivers * num_transmitters), dtype=np.uint16)

    # Save the data to a file
    with open(output_file, "wb") as f:
        for sample in data:
            f.write(struct.pack('<' + 'H' * (num_receivers * num_transmitters), *sample))

    # Confirm the file size
    actual_file_size = os.path.getsize(output_file) / (1024 * 1024)  # Convert to MB
    print(f"Data saved to {output_file}")
    print(f"Actual file size: {actual_file_size:.2f} MB")

def main():
    # Configuration
    file_sizes_mb = [30,100]  # Desired file sizes in megabytes
    num_receivers = 4            # Number of receivers
    num_transmitters = 3         # Number of transmitters
    sampling_rate_msps = 25      # Sampling rate in MSPS (Mega Samples Per Second)
    if_bandwidth_mhz = 10        # IF bandwidth in MHz

    # Generate and save fake radar data for each file size
    for file_size_mb in file_sizes_mb:
        output_file = f"radar_data_{file_size_mb}MB.bin"
        generate_fake_radar_data(file_size_mb, num_receivers, num_transmitters, sampling_rate_msps, if_bandwidth_mhz, output_file)

if __name__ == "__main__":
    main()
