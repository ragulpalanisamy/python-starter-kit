# ============================================
# PRACTICAL FUNCTION EXAMPLES
# ============================================

print("=" * 60)
print("PRACTICAL FUNCTION EXAMPLES")
print("=" * 60)

# Example 1: Email validator
print("\n1️⃣  EMAIL VALIDATOR")
print("-" * 60)

def is_valid_email(email):
    """Check if email is valid"""
    if "@" in email and "." in email.split("@")[1]:
        return True
    return False

emails = ["user@example.com", "invalid.email", "test@domain.co"]
for email in emails:
    status = "✅ Valid" if is_valid_email(email) else "❌ Invalid"
    print(f"{email}: {status}")

# Example 2: Temperature converter
print("\n2️⃣  TEMPERATURE CONVERTER")
print("-" * 60)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f = 77
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c}°C")

# Example 3: Password strength checker
print("\n3️⃣  PASSWORD STRENGTH CHECKER")
print("-" * 60)

def check_password_strength(password):
    """Check password strength"""
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("At least 8 characters")
    
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letter")
    
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letter")
    
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add number")
    
    if any(not c.isalnum() for c in password):
        score += 1
    else:
        feedback.append("Add special character")
    
    strength = ["Very Weak", "Weak", "Fair", "Good", "Strong"][score - 1] if score > 0 else "Very Weak"
    
    return strength, feedback

passwords = ["pass", "Password1", "P@ssw0rd!"]
for pwd in passwords:
    strength, tips = check_password_strength(pwd)
    print(f"'{pwd}': {strength}")
    if tips:
        print(f"  Tips: {', '.join(tips)}")

# Example 4: Calculate discount
print("\n4️⃣  DISCOUNT CALCULATOR")
print("-" * 60)

def calculate_discount(price, discount_percent=0):
    """Calculate final price after discount"""
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price, discount_amount

price = 1000
final, discount = calculate_discount(price, 20)
print(f"Original: ₹{price}")
print(f"Discount (20%): ₹{discount}")
print(f"Final: ₹{final}")

# Example 5: Find prime numbers
print("\n5️⃣  PRIME NUMBER FINDER")
print("-" * 60)

def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(limit):
    """Get all prime numbers up to limit"""
    return [n for n in range(2, limit + 1) if is_prime(n)]

primes = get_primes(20)
print(f"Prime numbers up to 20: {primes}")

# Example 6: String formatter
print("\n6️⃣  STRING FORMATTER")
print("-" * 60)

def format_name(first, last, title=""):
    """Format person's name"""
    if title:
        return f"{title} {first} {last}"
    return f"{first} {last}"

def format_phone(number):
    """Format phone number"""
    # Remove non-digits
    digits = ''.join(filter(str.isdigit, number))
    # Format as (XXX) XXX-XXXX
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return number

print(format_name("Ragul", "Palanisamy"))
print(format_name("Ragul", "Palanisamy", "Dr."))
print(format_phone("1234567890"))

# Example 7: List statistics
print("\n7️⃣  LIST STATISTICS")
print("-" * 60)

def get_stats(numbers):
    """Calculate statistics for a list of numbers"""
    if not numbers:
        return None
    
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }

data = [10, 20, 30, 40, 50]
stats = get_stats(data)
print(f"Data: {data}")
for key, value in stats.items():
    print(f"  {key.capitalize()}: {value}")

# Example 8: Grade calculator
print("\n8️⃣  GRADE CALCULATOR")
print("-" * 60)

def calculate_grade(marks):
    """Calculate grade based on marks"""
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

def get_grade_report(student_name, marks):
    """Generate grade report"""
    grade = calculate_grade(marks)
    status = "Pass" if marks >= 60 else "Fail"
    
    return {
        "name": student_name,
        "marks": marks,
        "grade": grade,
        "status": status
    }

report = get_grade_report("Ragul", 85)
print(f"Student: {report['name']}")
print(f"Marks: {report['marks']}")
print(f"Grade: {report['grade']}")
print(f"Status: {report['status']}")

# Example 9: Shopping cart
print("\n9️⃣  SHOPPING CART")
print("-" * 60)

def add_to_cart(cart, item, price, quantity=1):
    """Add item to shopping cart"""
    cart[item] = {"price": price, "quantity": quantity}
    return cart

def calculate_total(cart):
    """Calculate total cart value"""
    total = sum(item["price"] * item["quantity"] for item in cart.values())
    return total

cart = {}
add_to_cart(cart, "Apple", 50, 3)
add_to_cart(cart, "Banana", 30, 5)
add_to_cart(cart, "Mango", 80, 2)

print("Shopping Cart:")
for item, details in cart.items():
    print(f"  {item}: ₹{details['price']} × {details['quantity']}")

total = calculate_total(cart)
print(f"Total: ₹{total}")

# Example 10: Text analyzer
print("\n🔟 TEXT ANALYZER")
print("-" * 60)

def analyze_text(text):
    """Analyze text and return statistics"""
    words = text.split()
    
    return {
        "characters": len(text),
        "words": len(words),
        "sentences": text.count('.') + text.count('!') + text.count('?'),
        "vowels": sum(1 for c in text.lower() if c in 'aeiou'),
        "consonants": sum(1 for c in text.lower() if c.isalpha() and c not in 'aeiou')
    }

text = "Hello World! This is Python programming."
analysis = analyze_text(text)
print(f"Text: {text}")
print("Analysis:")
for key, value in analysis.items():
    print(f"  {key.capitalize()}: {value}")

print()
