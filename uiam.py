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

x = ulam_sequence(1, 2, 20)
print(x)

a = [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69]
print(a)
#   test.assert_equals(ulam_sequence(1, 2, 20), a)