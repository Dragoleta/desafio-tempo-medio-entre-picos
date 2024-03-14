test_tuple = []

picos = []


def read_dataset(path: str):
    read = open(path, "r")
    for line in read:
        numbers = line.strip()
        test_tuple.append(int(numbers))
    read.close()


def check_if_peaks_colide(peaks: list, checking_distance: int):
    popped = False

    for i in range(len(peaks) - 1):
        if peaks[i] - peaks[i + 1] > -checking_distance:
            popped = True
            if test_tuple[peaks[i]] > test_tuple[peaks[i + 1]]:
                peaks.pop(i + 1)
            else:
                peaks.pop(i)
            break

    if popped is True:
        check_if_peaks_colide(peaks=peaks, checking_distance=checking_distance)

    return peaks


def find_time_media(lista: tuple):
    time_sum = 0

    for pos in range(len(lista) - 1):
        time = lista[pos] - lista[pos + 1]
        time_sum += time

    divisor = len(lista) - 1
    return (time_sum * -1) / divisor


def find_all_peaks():
    for pos, number in enumerate(test_tuple):
        if 50 > number:
            continue
        if test_tuple[pos - 1] > number or number < test_tuple[pos + 1]:
            continue
        picos.append(pos)
    return picos


def convert_seconds(seconds: int):
    minutes = int(seconds // 60)
    remaining_seconds = int(seconds % 60)
    return f"{minutes:02d}:{remaining_seconds:02d}"


read_dataset("exemplo.txt")
every_peak = find_all_peaks()
true_peaks = check_if_peaks_colide(peaks=every_peak.copy(), checking_distance=5)
time_interval = find_time_media(true_peaks)

print("Todos os picos: ", every_peak)
print("Picos verdadeiros: ", true_peaks)
print("Intervalo de tempo: ", time_interval)
print("intervalo de tempo em minutos: ", convert_seconds(time_interval))
