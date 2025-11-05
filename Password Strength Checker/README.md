# Password Strength Checker

## Author

**Devon Morris**

## About

A simple Python utility that evaluates the strength of a given password using [zxcvbn](https://github.com/dropbox/zxcvbn), an open-source library developed by Dropbox. zxcvbn uses real-world data to estimate how easily a password could be cracked through dictionary, brute-force, or pattern-based attacks. These are common methods used by attackers to guess passwords and obtain sensitive information, which is why creating strong, unpredictable passwords is important.

Password strength determines how resistant a password is to being guessed or cracked by attackers. A variety of factors contribute to a strong password, and the general standard is:

- Length over complexity: Minimum of 8 characters, ideally 15+ for stronger protection.
- Use a mix of characters: Combine letters, numbers, symbols, and spaces to increase randomness.
- Uppercase/lowercase: Use both if possible, though less important today.
- Avoid common passwords: Don’t use passwords found in breaches, dictionary lists, or simple predictable phrases.

## Features

- Scores password 0-4 based on strength
- Estimates how long it would take to crack a password
- Detects dictionary words, patterns, and weak combinations
- Provides clear feedback to help users create stronger passwords

## How to Run (Tested with Python 3.14.0)

```bash
pip install -r requirements.txt
python main.py
```

## Example

### Very Weak (0)

```bash
Enter a password to check its strength: Test
The password 'Test':
Score (0-4): 0
Crack Time (seconds): 0.0187
Feedback: {'warning': 'This is a top-100 common password.', 'suggestions': ['Add another word or two. Uncommon words are better.', "Capitalization doesn't help very much."]}
```

### Weak (1)

```bash
Enter a password to check its strength: WeakPass
The password 'WeakPass':
Score (0-4): 1
Crack Time (seconds): 61.4632
Feedback: {'warning': '', 'suggestions': ['Add another word or two. Uncommon words are better.', "Capitalization doesn't help very much."]}
```

### Fair (2)

```bash
Enter a password to check its strength: M0unTainViews
The password 'M0unTainViews':
Score (0-4): 2
Crack Time (seconds): 9420.4688
Feedback: {'warning': '', 'suggestions': ['Add another word or two. Uncommon words are better.', "Predictable substitutions like '@' instead of 'a' don't help very much."]}
```

### Strong (3)

```bash
Enter a password to check its strength: Flashes123!
The password 'Flashes123!':
Score (0-4): 3
Crack Time (seconds): 12525.16
Feedback: {'warning': '', 'suggestions': []}
```

### Very Strong (4)

```bash
Enter a password to check its strength: 3x!r3m31yH!4rdt063t
The password '3x!r3m31yH!4rdt063t':
Score (0-4): 4
Crack Time (seconds): 240000000000001
Feedback: {'warning': '', 'suggestions': []}
```

## Full Example zxcvbn Output

```bash
The password 'test':
Score (0-4): 0
Crack Time (seconds): 0.0094
Feedback: {'warning': 'This is a top-100 common password.', 'suggestions': ['Add another word or two. Uncommon words are better.']}
{
    'password': 'test',
    'guesses': Decimal('94'),
    'guesses_log10': 1.9731278535996983,
    'sequence': [
        {
            'pattern': 'dictionary',
            'i': 0,
            'j': 3,
            'token': 'test',
            'matched_word': 'test',
            'rank': 93,
            'dictionary_name': 'passwords',
            'reversed': False,
            'l33t': False,
            'base_guesses': 93,
            'uppercase_variations': 1,
            'l33t_variations': 1,
            'guesses': 93,
            'guesses_log10': 1.968482948553935
        }
    ],
    'calc_time': datetime.timedelta(microseconds=757),
    'crack_times_seconds': {
        'online_throttling_100_per_hour': Decimal('3384.000000000000187849735767'),
        'online_no_throttling_10_per_second': Decimal('9.4'),
        'offline_slow_hashing_1e4_per_second': Decimal('0.0094'),
        'offline_fast_hashing_1e10_per_second': Decimal('9.4E-9')
    },
    'crack_times_display': {
        'online_throttling_100_per_hour': '56 minutes',
        'online_no_throttling_10_per_second': '9 seconds',
        'offline_slow_hashing_1e4_per_second': 'less than a second',
        'offline_fast_hashing_1e10_per_second': 'less than a second'
    },
    'score': 0,
    'feedback': {
        'warning': 'This is a top-100 common password.',
        'suggestions': [
            'Add another word or two. Uncommon words are better.'
        ]
    }
}
```
