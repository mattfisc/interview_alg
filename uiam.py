def ulam_sequence(u0, u1, n):
    x = u0
    y = u1

    arr = [u0, u1]
    duplicates = [u0, u1]

    sum = u0 + u1
    smallest = sum + sum

    while len(arr) < n:
        for x in range(len(arr) - 1):

            for y in range(x + 1, len(arr)):
                sum = arr[x]+arr[y]

                if sum in duplicates:  # no duplicates
                    continue
                else:
                    if smallest > sum and arr[x] != arr[y]:
                        smallest = sum
                        print(smallest)

                duplicates.append(sum)
        arr.append(smallest)
        smallest = arr[y]**3

    return arr

x = ulam_sequence(1, 3, 60)
print(x)
#[1, 3, 4, 5, 6, 8, 10, 12, 17, 21, 23, 28, 32, 34, 39, 43, 48, 52, 54, 59, 63, 68, 72, 74, 79, 83, 98, 99, 101, 110, 114, 121, 125, 132, 136, 139, 143, 145, 152, 161, 165, 172, 176, 187, 192, 196, 201, 205, 212, 216, 223, 227, 232, 234, 236, 243, 247, 252, 256, 258]
