import pandas as pd
import uuid
import random


def random_uuid(number_of_users):
    return [str(uuid.uuid4()) for _ in range(number_of_users)]


def random_user_uuid():
    return str(uuid.uuid4()) if random.random() > 0.8 else None


def random_listing_id():
    return str(random.randint(100000, 999999))


def random_land_reg_type():
    return random.choice(['flat', 'detached', 'terraced', 'semi-detached'])


def random_transaction_type():
    return random.choice(['sale', 'rent'])


def random_listing_status(transaction_type):
    if transaction_type == 'sale':
        return random.choice(['for-sale', 'sale-under-offer', 'sold'])
    else:
        return random.choice(['to-rent', 'rent-under-offer', 'rented'])


def random_price():
    return round(random.uniform(80000, 2000000))


def random_num_beds():
    return random.randint(0, 10)


def random_num_baths():
    return random.randint(0, 5)


def random_postcode():
    return random.choice(["SE8 5DR", "DD10 0RT", "EH6 6LS"])


def get_latitude_longitude(postcode):
    postcode_map = {
        "SE8 5DR": (56.8441, -2.278605),
        "DD10 0RT": (55.977406, -3.175213),
        "EH6 6LS": (51.490513, -0.042433)
    }
    return postcode_map[postcode]


def create_random_listings(number_of_listings):
    listings = []
    for _ in range(number_of_listings):
        postcode = random_postcode()
        postcode_latitude = get_latitude_longitude(postcode)[0]
        postcode_longitude = get_latitude_longitude(postcode)[1]
        transaction_type = random_transaction_type()
        listing_status = random_listing_status(transaction_type)
        listings.append(
            {
                "listing_id": random_listing_id(),
                "price": random_price(),
                "num_beds": random_num_beds(),
                "num_baths": random_num_baths(),
                "land_reg_type": random_land_reg_type(),
                "transaction_type": transaction_type,
                "listing_status": listing_status,
                "postcode": postcode,
                "postcode_latitude": postcode_latitude,
                "postcode_longitude": postcode_longitude,
                "balcony": random.randint(0, 1),
                "bath": random.randint(0, 1),
                "conservatory": random.randint(0, 1),
                "cottage": random.randint(0, 1),
                "driveway": random.randint(0, 1),
                "en_suite": random.randint(0, 1),
                "garage": random.randint(0, 1),
                "garden": random.randint(0, 1),
                "kitchen_island": random.randint(0, 1),
                "patio": random.randint(0, 1),
                "period_property": random.randint(0, 1),
                "new_home": random.randint(0, 1)
            }
        )
    return listings


def random_sent_lead(lsrp_click):
    if lsrp_click == 1:
        return 1 if random.random() < 0.10 else 0
    else:
        return 1 if random.random() < 0.005 else 0


def random_listing_saved(lsrp_click):
    if lsrp_click == 1:
        return 1 if random.random() < 0.25 else 0
    else:
        return 0


def random_time_spent(lsrp_click):
    if lsrp_click == 1:
        return random.uniform(1, 400)
    else:
        return 0


def random_number_of_times_viewed(lsrp_click):
    if lsrp_click == 1:
        return random.randint(1, 10)
    else:
        return 0


def random_lsrp_click():
    return 1 if random.random() <= 0.1 else 0


def generate_user_listing_interactions(
    max_number_of_interactions,
    number_of_users,
    number_of_listings
):

    if max_number_of_interactions > number_of_listings:
        print(f"NB! Cannot have more interactions than there are listings. Setting max_number_of_interactions = {number_of_listings}")
        max_number_of_interactions = number_of_listings

    random_users = random_uuid(number_of_users)
    random_listings = create_random_listings(number_of_listings)

    interactions = []

    for random_user in random_users:
        number_of_interactions = random.randint(1, max_number_of_interactions)
        random_listings_interacted = random.sample(random_listings, number_of_interactions)
        for random_listing in random_listings_interacted:
            lsrp_view = 1
            lsrp_click = random_lsrp_click()
            time_spent = random_time_spent(lsrp_click)
            listing_saved = random_listing_saved(lsrp_click)
            num_views = random_number_of_times_viewed(time_spent)
            sent_lead = random_sent_lead(lsrp_click)

            interactions.append(
                {
                    "anonymous_id": random_user,
                    "listing_id": random_listing["listing_id"],
                    "sent_lead": sent_lead,
                    "listing_saved": listing_saved,
                    "time_spent_on_listing": time_spent,
                    "number_of_times_property_viewed": num_views,
                    "lsrp_click": lsrp_click,
                    "lsrp_view": lsrp_view,
                    "land_reg_type": random_listing["land_reg_type"],
                    "transaction_type": random_listing["transaction_type"],
                    "listing_status": random_listing["listing_status"],
                    "price": random_listing["price"],
                    "num_beds": random_listing["num_beds"],
                    "num_baths": random_listing["num_baths"],
                    "postcode": random_listing["postcode"],
                    "postcode_latitude": random_listing["postcode_latitude"],
                    "postcode_longitude": random_listing["postcode_longitude"],
                    "balcony": random_listing["balcony"],
                    "bath": random_listing["bath"],
                    "conservatory": random_listing["conservatory"],
                    "cottage": random_listing["cottage"],
                    "driveway": random_listing["driveway"],
                    "en_suite": random_listing["en_suite"],
                    "garage": random_listing["garage"],
                    "garden": random_listing["garden"],
                    "kitchen_island": random_listing["kitchen_island"],
                    "patio": random_listing["patio"],
                    "period_property": random_listing["period_property"],
                    "new_home": random_listing["new_home"],
                }
            )
    return pd.DataFrame(interactions)
