CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS notions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    context TEXT,
    description TEXT,
    status TEXT NOT NULL CHECK (status IN ('À apprendre', 'Acquise')),
    FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS notions_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    notion_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    FOREIGN KEY (notion_id) REFERENCES notions (id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags (id) ON DELETE CASCADE,
    UNIQUE (notion_id, tag_id)
);
