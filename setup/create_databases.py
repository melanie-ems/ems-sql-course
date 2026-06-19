import sqlite3
import os

os.makedirs("databases", exist_ok=True)

# ============================================================
# Schema 1: Library
# Tables: Member, Book, Loan
# AQA Section 4.10 — Fundamentals of Databases
# ============================================================

conn = sqlite3.connect("databases/library.db")
c = conn.cursor()

c.executescript("""
-- --------------------------------------------------------
-- Drop tables if they already exist (safe to re-run)
-- --------------------------------------------------------
DROP TABLE IF EXISTS Loan;
DROP TABLE IF EXISTS Book;
DROP TABLE IF EXISTS Member;

-- --------------------------------------------------------
-- Member
-- Represents a library member who can borrow books
-- --------------------------------------------------------
CREATE TABLE Member (
    MemberID    INTEGER PRIMARY KEY,
    FirstName   TEXT    NOT NULL,
    LastName    TEXT    NOT NULL,
    Email       TEXT    UNIQUE NOT NULL,
    JoinDate    TEXT    NOT NULL,
    Active      INTEGER NOT NULL DEFAULT 1  -- 1 = active, 0 = inactive
);

-- --------------------------------------------------------
-- Book
-- Represents a book held in the library's collection
-- --------------------------------------------------------
CREATE TABLE Book (
    BookID      INTEGER PRIMARY KEY,
    Title       TEXT    NOT NULL,
    Author      TEXT    NOT NULL,
    Genre       TEXT    NOT NULL,
    YearPublished INTEGER,
    Available   INTEGER NOT NULL DEFAULT 1  -- 1 = on shelf, 0 = on loan
);

-- --------------------------------------------------------
-- Loan
-- Records which member has borrowed which book and when
-- A NULL ReturnDate means the book is still on loan
-- --------------------------------------------------------
CREATE TABLE Loan (
    LoanID      INTEGER PRIMARY KEY,
    MemberID    INTEGER NOT NULL,
    BookID      INTEGER NOT NULL,
    LoanDate    TEXT    NOT NULL,
    ReturnDate  TEXT,               -- NULL if not yet returned
    FOREIGN KEY (MemberID) REFERENCES Member(MemberID),
    FOREIGN KEY (BookID)   REFERENCES Book(BookID)
);

-- --------------------------------------------------------
-- Sample data — Member
-- --------------------------------------------------------
INSERT INTO Member VALUES (1,  'Alice',   'Smith',    'alice.smith@email.com',    '2021-09-01', 1);
INSERT INTO Member VALUES (2,  'Ben',     'Jones',    'ben.jones@email.com',      '2021-09-01', 1);
INSERT INTO Member VALUES (3,  'Chloe',   'Ahmed',    'chloe.ahmed@email.com',    '2022-01-15', 1);
INSERT INTO Member VALUES (4,  'Dylan',   'Patel',    'dylan.patel@email.com',    '2022-03-10', 1);
INSERT INTO Member VALUES (5,  'Emma',    'Wilson',   'emma.wilson@email.com',    '2022-09-01', 1);
INSERT INTO Member VALUES (6,  'Finn',    'OBrien',   'finn.obrien@email.com',    '2023-01-20', 0);
INSERT INTO Member VALUES (7,  'Grace',   'Lee',      'grace.lee@email.com',      '2023-09-01', 1);
INSERT INTO Member VALUES (8,  'Harry',   'Evans',    'harry.evans@email.com',    '2023-09-01', 1);
INSERT INTO Member VALUES (9,  'Isla',    'Brown',    'isla.brown@email.com',     '2024-01-08', 1);
INSERT INTO Member VALUES (10, 'Jack',    'Taylor',   'jack.taylor@email.com',    '2024-02-14', 1);

-- --------------------------------------------------------
-- Sample data — Book
-- --------------------------------------------------------
INSERT INTO Book VALUES (1,  '1984',                         'George Orwell',        'Dystopian',  1949, 0);
INSERT INTO Book VALUES (2,  'Brave New World',              'Aldous Huxley',        'Dystopian',  1932, 1);
INSERT INTO Book VALUES (3,  'To Kill a Mockingbird',        'Harper Lee',           'Fiction',    1960, 1);
INSERT INTO Book VALUES (4,  'The Great Gatsby',             'F. Scott Fitzgerald',  'Fiction',    1925, 0);
INSERT INTO Book VALUES (5,  'Dune',                         'Frank Herbert',        'Sci-Fi',     1965, 1);
INSERT INTO Book VALUES (6,  'The Hitchhikers Guide',        'Douglas Adams',        'Sci-Fi',     1979, 0);
INSERT INTO Book VALUES (7,  'Harry Potter and the Philosopher''s Stone', 'J.K. Rowling', 'Fantasy', 1997, 1);
INSERT INTO Book VALUES (8,  'The Hobbit',                   'J.R.R. Tolkien',       'Fantasy',    1937, 1);
INSERT INTO Book VALUES (9,  'Pride and Prejudice',          'Jane Austen',          'Romance',    1813, 0);
INSERT INTO Book VALUES (10, 'Frankenstein',                 'Mary Shelley',         'Horror',     1818, 1);
INSERT INTO Book VALUES (11, 'The Hunger Games',             'Suzanne Collins',      'Dystopian',  2008, 1);
INSERT INTO Book VALUES (12, 'Animal Farm',                  'George Orwell',        'Satire',     1945, 1);

-- --------------------------------------------------------
-- Sample data — Loan
-- Completed loans have a ReturnDate; active loans have NULL
-- --------------------------------------------------------
INSERT INTO Loan VALUES (1,  1,  1,  '2024-01-10', '2024-01-24');
INSERT INTO Loan VALUES (2,  2,  4,  '2024-01-15', '2024-01-29');
INSERT INTO Loan VALUES (3,  3,  6,  '2024-02-01', '2024-02-15');
INSERT INTO Loan VALUES (4,  4,  9,  '2024-02-10', '2024-02-24');
INSERT INTO Loan VALUES (5,  1,  6,  '2024-03-01', '2024-03-15');
INSERT INTO Loan VALUES (6,  5,  1,  '2024-03-10', NULL);
INSERT INTO Loan VALUES (7,  7,  4,  '2024-03-12', NULL);
INSERT INTO Loan VALUES (8,  8,  9,  '2024-03-20', NULL);
INSERT INTO Loan VALUES (9,  2,  3,  '2024-04-01', '2024-04-15');
INSERT INTO Loan VALUES (10, 3,  5,  '2024-04-05', '2024-04-19');
INSERT INTO Loan VALUES (11, 9,  7,  '2024-04-10', '2024-04-24');
INSERT INTO Loan VALUES (12, 10, 2,  '2024-04-15', '2024-04-29');
INSERT INTO Loan VALUES (13, 6,  8,  '2024-04-20', '2024-05-04');
INSERT INTO Loan VALUES (14, 7,  11, '2024-05-01', '2024-05-15');
INSERT INTO Loan VALUES (15, 4,  12, '2024-05-10', NULL);
""")

conn.commit()
conn.close()
print("✓ databases/library.db created successfully")
print("  Tables: Member (10 rows), Book (12 rows), Loan (15 rows)")
