# Assignment 1: Design Your Own Class (Smartphone) 🏗️

# Base Class: Smartphone
class Smartphone:
    """
    Represents a generic smartphone with basic functionalities.
    Demonstrates encapsulation by bundling data (attributes) and methods
    that operate on the data within a single unit.
    """
    def __init__(self, brand, model, os, storage_gb, battery_percent=100):
        """
        Constructor to initialize a Smartphone object.

        Args:
            brand (str): The brand of the smartphone (e.g., "Samsung", "Apple").
            model (str): The model name of the smartphone (e.g., "Galaxy S23", "iPhone 15 Pro").
            os (str): The operating system (e.g., "Android", "iOS").
            storage_gb (int): The internal storage in GB.
            battery_percent (int): The current battery percentage (default: 100).
        """
        self._brand = brand  # Protected attribute
        self._model = model  # Protected attribute
        self.os = os
        self.storage_gb = storage_gb
        self._battery_percent = battery_percent # Encapsulated attribute

    def __str__(self):
        """Returns a string representation of the smartphone."""
        return f"{self._brand} {self._model} ({self.os}) - {self.storage_gb}GB"

    def make_call(self, number):
        """Simulates making a phone call."""
        if self._battery_percent > 5:
            self._battery_percent -= 2
            print(f"{self._brand} {self._model} is calling {number}.")
        else:
            print(f"Low battery on {self._model}, cannot make call.")

    def charge_battery(self, duration_minutes):
        """Charges the phone for a given duration."""
        self._battery_percent = min(100, self._battery_percent + (duration_minutes // 5))
        print(f"{self._model} charged for {duration_minutes} mins. Battery: {self._battery_percent}%")

    def get_battery_status(self):
        """Returns the current battery percentage."""
        return self._battery_percent

# Inherited Class: AndroidPhone (demonstrates inheritance)
class AndroidPhone(Smartphone):
    """
    Represents an Android smartphone, inheriting from Smartphone.
    Adds a specific attribute for Android versions.
    """
    def __init__(self, brand, model, android_version, storage_gb, battery_percent=100):
        """
        Constructor for AndroidPhone, calling the parent constructor.
        """
        super().__init__(brand, model, "Android", storage_gb, battery_percent)
        self.android_version = android_version

    def install_app(self, app_name):
        """Simulates installing an app from the Play Store."""
        print(f"{self._model} (Android {self.android_version}) installing {app_name} from Google Play Store.")

# Inherited Class: iPhone (demonstrates inheritance and polymorphism)
class iPhone(Smartphone):
    """
    Represents an iPhone, inheriting from Smartphone.
    Adds a specific attribute for iOS versions and overrides a method.
    """
    def __init__(self, model, ios_version, storage_gb, battery_percent=100):
        """
        Constructor for iPhone, setting brand to "Apple" and OS to "iOS".
        """
        super().__init__("Apple", model, "iOS", storage_gb, battery_percent)
        self.ios_version = ios_version

    def install_app(self, app_name):
        """Simulates installing an app from the App Store (polymorphic method)."""
        print(f"{self._model} (iOS {self.ios_version}) installing {app_name} from Apple App Store.")

# --- Demonstrating Assignment 1 ---
print("--- Assignment 1: Smartphone Class ---")
my_android = AndroidPhone("Samsung", "Galaxy S23", "14", 128)
my_iphone = iPhone("iPhone 15 Pro", "17.5", 256, 80)

print(my_android)
my_android.make_call("555-1234")
my_android.install_app("WhatsApp")
my_android.charge_battery(30)
print(f"Battery status: {my_android.get_battery_status()}%")
print("-" * 20)

print(my_iphone)
my_iphone.make_call("555-5678")
my_iphone.install_app("Instagram")
print(f"Battery status: {my_iphone.get_battery_status()}%")
print("=" * 40)

# Assignment 2: Polymorphism Challenge! 🎭

# Base class for vehicles
class Vehicle:
    """Base class for all vehicles with a common 'move' action."""
    def move(self):
        """Abstract method to be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement this method")

# Subclass: Car
class Car(Vehicle):
    """A car moves by driving."""
    def move(self):
        """Car-specific move action."""
        print("Driving 🚗")

# Subclass: Plane
class Plane(Vehicle):
    """A plane moves by flying."""
    def move(self):
        """Plane-specific move action."""
        print("Flying ✈️")

# Subclass: Boat
class Boat(Vehicle):
    """A boat moves by sailing."""
    def move(self):
        """Boat-specific move action."""
        print("Sailing ⛵")

# --- Demonstrating Assignment 2 (Polymorphism) ---
print("--- Assignment 2: Polymorphism Challenge ---")

# Create a list of different vehicle objects
vehicles = [Car(), Plane(), Boat()]

# Iterate through the list and call the 'move()' method on each object.
# Even though the method call is the same, the actual behavior is different
# depending on the object's type. This is polymorphism!
for vehicle in vehicles:
    vehicle.move()

print("=" * 40)
