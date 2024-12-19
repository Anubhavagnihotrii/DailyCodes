def main():
    n = 1111
    rem = 0
    num = n
    unique_divisors = set()
    
    while n > 0:
        rem = n % 10
        if rem == 0:
            n //= 10
            continue
        if num % rem == 0:
            unique_divisors.add(rem)
        n //= 10

    # Output the size of the set
    print(len(unique_divisors))

if __name__ == "__main__":
    main()
