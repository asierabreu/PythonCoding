from query_builder import QueryBuilder

# Example 1: Simple query
simple_query = (QueryBuilder()
    .select("id", "name", "email")
    .from_table("users")
    .where("status = 'active'")
    .order_by("name")
    .limit(10)
    .build())

print("Simple Query:")
print(simple_query.to_sql())

# Example 2: Complex query with joins and aggregations
complex_query = (QueryBuilder()
    .select("u.name", "COUNT(o.id) as order_count", "SUM(o.total) as total_spent")
    .from_table("users u")
    .left_join("orders o", "u.id = o.user_id")
    .where("u.created_at >= '2024-01-01'")
    .where("u.country = 'US'")
    .group_by("u.id", "u.name")
    .having("COUNT(o.id) > 5")
    .order_by("total_spent DESC")
    .limit(20)
    .build())

print("Complex Query:")
print(complex_query.to_sql())