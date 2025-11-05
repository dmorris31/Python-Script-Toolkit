# Password Strength Checker
# A simple tool to evaluate the strength of a given password.
# Devon Morris
# 11/5/2025

from zxcvbn import zxcvbn

if __name__ == "__main__":
    test_password = input("Enter a password to check its strength: ")
    result = zxcvbn(test_password)
    print(f"The password '{test_password}': ")
    print(f"Score (0-4): {result['score']}")
    print(
        f"Crack Time (seconds): {result['crack_times_seconds']['offline_slow_hashing_1e4_per_second']}")
    print(f"Feedback: {result['feedback']}")
