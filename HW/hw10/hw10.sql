CREATE TABLE parents AS
  SELECT "ace" AS parent, "bella" AS child UNION
  SELECT "ace"          , "charlie"        UNION
  SELECT "daisy"        , "hank"           UNION
  SELECT "finn"         , "ace"            UNION
  SELECT "finn"         , "daisy"          UNION
  SELECT "finn"         , "ginger"         UNION
  SELECT "ellie"        , "finn";

CREATE TABLE dogs AS
  SELECT "ace" AS name, "long" AS fur, 26 AS height UNION
  SELECT "bella"      , "short"      , 52           UNION
  SELECT "charlie"    , "long"       , 47           UNION
  SELECT "daisy"      , "long"       , 46           UNION
  SELECT "ellie"      , "short"      , 35           UNION
  SELECT "finn"       , "curly"      , 32           UNION
  SELECT "ginger"     , "short"      , 28           UNION
  SELECT "hank"       , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  select child from parents, dogs where parent=name order by -height
  ;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  select name, size from dogs, sizes where min<height and height<=max;


-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  SELECT a.child as sib1, b.child as sib2 from parents as a, parents as b where a.parent=b.parent and a.child<b.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, " || sib1 || " and " || sib2 || ", have the same size: " || a.size from siblings, size_of_dogs as a, size_of_dogs as b where sib1=a.name and sib2=b.name and a.size=b.size;


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  select fur, max(height)-min(height) from dogs group by fur having min(height)>=0.7*avg(height) and max(height)<=1.3*avg(height);
