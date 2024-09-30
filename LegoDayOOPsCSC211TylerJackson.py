from typing import List, Optional
import random, time


# class to define lego set functionality
class LegoSet:
    def __init__(self, set_name: str, piece_count: int, theme: str):
        self.set_name = set_name
        self.piece_count = piece_count
        self.theme = theme
        self.built_pieces = 0

    # method to set up build for lego sets
    def build(self, pieces_to_build: int) -> None:
        """Simulates building a part of the Lego set."""
        if pieces_to_build + self.built_pieces > self.piece_count:
            print(
                f"Cannot build {pieces_to_build} pieces. Only {self.piece_count - self.built_pieces} pieces left."
            )
        else:
            self.built_pieces += pieces_to_build
            print(
                f"Built {pieces_to_build} pieces of the {self.set_name}. Total built: {self.built_pieces}/{self.piece_count}"
            )

        if self.built_pieces == self.piece_count:
            print(f"\nCongratulations! You have completed the {self.set_name} set.")

    # checks progress of lego set build
    def progress(self) -> None:
        """Displays the current progress of the build."""
        print(
            f"Progress of {self.set_name}: {self.built_pieces}/{self.piece_count} pieces built."
        )


# class to get random legoset to build
class RandomBuild(LegoSet):
    def __init__(
        self,
        set_name: str,
        piece_count: int,
        theme: str,
        item_to_build: Optional[str] = None,
    ):
        super().__init__(set_name, piece_count, theme)
        self.item_to_build = item_to_build

    # accesses build for random build
    def build(self, pieces_to_build: int) -> None:
        """Builds either the whole set or a specific item if provided."""
        if self.item_to_build:
            print(
                f"Building a custom {self.item_to_build} using {pieces_to_build} pieces from {self.set_name} set."
            )
        else:
            print(f"Building the standard {self.set_name} set.")
        super().build(pieces_to_build)

    # displays what content Tyler is Watching on Lego Day
    def watch_content(self, content_type: str) -> None:
        """Simulates watching Lego-related content."""
        print(f"Now watching a Lego {content_type}. Enjoy your Lego Day!")


# class to define lego collection
class LegoCollection:
    def __init__(self):
        self.collection: List[LegoSet] = []

    # adds lego sets
    def add_set(self, lego_set: LegoSet) -> None:
        """Adds a Lego set to the collection."""
        self.collection.append(lego_set)
        print(f"Added {lego_set.set_name} to your collection.")

    # removes lego sets
    def remove_set(self, set_name: str) -> None:
        """Removes a Lego set from the collection."""
        self.collection = [
            lego_set for lego_set in self.collection if lego_set.set_name != set_name
        ]
        print(f"Removed {set_name} from your collection.")

    # displays what is in the collection
    def show_collection(self) -> None:
        """Displays all Lego sets in the collection."""
        if not self.collection:
            print("\nYour Lego collection is empty.")
        else:
            print("\nYour Lego Collection:")
            for lego_set in self.collection:
                print(
                    f"- {lego_set.set_name} ({lego_set.theme} theme) with {lego_set.piece_count} pieces"
                )


# plans out lego day
class LegoDayPlanner:
    def __init__(self, collection: LegoCollection):
        self.collection = collection

    # selects random build to plan out
    def plan_random_build(self) -> RandomBuild:
        """selects a Lego set from the collection and plans a build."""
        if not self.collection.collection:
            raise ValueError(
                "Your Lego collection is empty. Add some sets to your collection first!"
            )

        chosen_set = random.choice(self.collection.collection)
        item_to_build = self._pick_random_item()
        return RandomBuild(
            chosen_set.set_name, chosen_set.piece_count, chosen_set.theme, item_to_build
        )

    # picks radom items to build
    @staticmethod
    def _pick_random_item() -> str:
        """picks a random item to build."""
        items = ["Dragon", "Castle", "Spaceship", "Robot", "Car"]
        return random.choice(items)


# full day run through
def main():
    print("\nWelcome, Today is Lego Day in TylerLand! Let's get building!")
    print("First, We will add a couple sets to your collection! \n")
    my_collection = LegoCollection()
    time.sleep(3)
    my_collection.add_set(LegoSet("Ninjago City Gardens", 5685, "Ninjago"))
    my_collection.add_set(LegoSet("Hogwarts Castle", 6020, "Harry Potter"))
    time.sleep(3)
    my_collection.show_collection()
    time.sleep(1)

    # Planning a Lego Day build
    print("\nNow, let's continue out the day!\n")
    time.sleep(1)
    planner = LegoDayPlanner(my_collection)
    time.sleep(1)
    lego_day_set = planner.plan_random_build()
    time.sleep(1)
    lego_day_set.build(3000)  # Build a portion of the set
    time.sleep(3)
    lego_day_set.progress()  # Check progress
    time.sleep(1)
    lego_day_set.watch_content("movie")  # Watch a Lego movie
    time.sleep(1)

    # Building another portion of the same set
    print("")
    lego_day_set.build(2685)
    time.sleep(3)
    lego_day_set.progress()
    time.sleep(1)

    # Adding more sets and planning another Lego Day
    print("")
    my_collection.add_set(LegoSet("Millennium Falcon", 7541, "Star Wars"))
    time.sleep(1)
    lego_day_set_2 = planner.plan_random_build()
    time.sleep(1)
    lego_day_set_2.build(2000)
    time.sleep(1)
    lego_day_set_2.watch_content("cartoon")
    time.sleep(1)


if __name__ == "__main__":
    # run main
    main()
