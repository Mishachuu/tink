def main():
    mass = [1]  # вершины которые посетил
    ind = 1  # начальная вершина
    counts = 1
    while True:
        ind = (ind+15) % 2019
        if ind in mass:
            break
        mass.append(ind)
        counts += 1
    
    print(counts)


if __name__ == "__main__":
    main()
