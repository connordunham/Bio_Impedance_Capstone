import Bio_Impedance_Capstone.AD5933_LIB as BIS

ad5933 = BIS.AD5933(BIS.AD5933_ADDR, 1)

ad5933.print_read(BIS.CTRL_TEMP_MEASURE)




