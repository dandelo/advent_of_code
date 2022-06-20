import lib.commons as commons
import pandas as pd

input_file = commons.get_input_filename()
# input = commons.read_file_to_list(input_file)
with open(input_file) as myfile:
    mydata = (list(line.strip()) for line in myfile)
    df = pd.DataFrame(mydata)


def part_one(df):
    gamma = epsilon = ''
    for col in df.columns:
        counts = df[col].value_counts()
        gamma = gamma + str(counts.index[0])
        epsilon = epsilon + str(counts.index[-1])
    return int(gamma, 2) * int(epsilon, 2)


def part_two(df):
    df_gamma = df.copy(deep=True)
    df_epsilon = df.copy(deep=True)
    for col in df.columns:
        if len(df_gamma) > 1:
            counts = df_gamma[col].value_counts()
            most = counts.index[0]
            least = counts.index[-1]
            to_keep = most if counts[0] != counts[-1] else '1'
            df_gamma = df_gamma.loc[df_gamma[col]==to_keep]
        if len(df_epsilon) > 1:
            counts = df_epsilon[col].value_counts()
            most = counts.index[0]
            least = counts.index[-1]
            to_keep = least if counts[0] != counts[-1] else '0'
            df_epsilon = df_epsilon.loc[df_epsilon[col]==to_keep]

    oxygen_generator_rating = df_gamma.to_string(header=False, index=False).replace(' ', '')
    # print(oxygen_generator_rating)
    co2_scrubber_rating = df_epsilon.to_string(header=False, index=False).replace(' ', '')
    # print(co2_scrubber_rating)
    return(int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2))


print(part_one(df))
print(part_two(df))
