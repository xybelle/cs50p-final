-- Keep a log of any SQL queries you execute as you solve the mystery.

-- To see schema
.schema

-- Check for more info in the crime_scene_reports for theft that took place on 28th July, 2023
SELECT description
FROM crime_scene_reports
WHERE year = 2023 AND day = 28 AND month = 07;

-- Theft took place 10.15am at the bakery. There are 3 witnesses.

-- Check interviews of the 3 witnesses if there are more info
SELECT id, name, transcript
FROM interviews
WHERE year = 2023 AND month = 07 AND day = 28;

-- Ruth (withness) mentioned sometime within 10 mins of the theft, thief got into a car.
-- Eugene (withness) saw thief withdrawing some money on an ATM on Leggett Street.
-- Raymond (witness) saw thief called someone on the phone (< 1 minute). Asked the other person
    -- to purchase flight ticket for earliest flight out of Fiftyville on 29th July.

-- Get origin_airport_id of Fiftyville
SELECT * FROM airports;

-- | 8 | CSF | Fiftyville Regional Aiport | Fiftyville |

-- Check earliest flight out of Fiftyville and destination
SELECT * FROM flights
WHERE origin_airport_id = 8 AND year = 2023 AND month = 07 AND day = 29;

-- Earliest flight out of Fiftyville is flight_id: 36 followed by 43, 23, 53, 18

-- Check airport id 4 (destination).
SELECT * FROM airports
-- | 4 | LGA | LaGuardia Airport | New York City |

-- Check passengers who booked flight_id: 36, who may have also withdrew money from ATM on
    -- Leggett Street on the 28th, and made a phone call to someone with less than a minute
    -- duration, who may also be around the bakery around 10.
SELECT name, phone_number, license_plate FROM people
WHERE passport_number in (
    SELECT passport_number FROM passengers
    WHERE flight_id = 36
) AND id IN (
    SELECT person_id FROM bank_accounts
    WHERE account_number in (
        SELECT account_number FROM atm_transactions
        WHERE atm_location = 'Leggett Street' AND transaction_type = 'withdraw' AND year = 2023
            AND month = 07 AND day = 28
    )
) AND phone_number in (
    SELECT caller FROM phone_calls
    WHERE duration <= 60 AND year = 2023 AND month = 07 AND day = 28
) AND license_plate in (
    SELECT license_plate FROM bakery_security_logs
    WHERE year = 2023 AND month = 07 AND day = 28 AND hour = 10
);

-- Narrowed down to Taylor and Bruce

-- Check bakery security logs around what time both
SELECT license_plate, activity, hour, minute FROM bakery_security_logs
WHERE license_plate in ('1106N58', '94KL13X');

-- Theft happened around 10.15am and Ruby (witness) said that sometime within 10 mins of the
    -- theft, the thief got into a car. Based on the security logs, the theif isn't Taylor
    -- they left or exited the premise at 10.35am which is well beyong the 10 mins Ruby mentioned.
-- Primary suspect is now Bruce.

-- Check who Bruce called
SELECT name FROM people
WHERE phone_number in (
    SELECT receiver FROM phone_calls
    WHERE caller = '(367) 555-5533' AND year = 2023 AND month = 07 AND day = 28
        AND duration <= 60
);

-- Bruce called Robin on the 28th July, 2023 and duration was less than a minute.
