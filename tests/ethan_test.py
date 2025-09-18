


def main():

    per_atom_data = read_atom_data(file)
    logs_file_data = read_log_data(file)
    dxa_file_data = read_dxa_data(file)

    plot_object = create_plot_object(subplots_thing=(4,4))

    plot_object.add(position=(1,1), data=per_atom_data)

    return None