def evaluate_performance(percentage):
    if percentage >= 90:
        print("Excellent performance")
    elif percentage >= 80:
        print("Very Good performance")
    elif percentage >= 70:
        print("Good performance")
    elif percentage >= 60:
        print("Average performance")
    else:
        print("Needs improvement")

percentage = float(input("Masukkan persentase siswa: "))
evaluate_performance(percentage)

