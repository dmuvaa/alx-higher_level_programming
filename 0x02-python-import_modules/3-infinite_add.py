#!/usr/bin/python3
#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    for value in sys.argv:
        if value != sys.argv[0]:
            add +=int(value)
    print(add)
