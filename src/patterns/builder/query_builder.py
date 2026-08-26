from sql_query import SQLQuery

class QueryBuilder:
    """Builder for SQL queries"""
    def __init__(self):
        self._query = SQLQuery()

    def select(self, *columns):
        """Add columns to SELECT clause"""
        self._query.select_columns.extend(columns)
        return self

    def from_table(self, table):
        """Set the FROM table"""
        self._query.from_table = table
        return self

    def join(self, table, on_condition, join_type="INNER"):
        """Add a JOIN clause"""
        join_clause = f"{join_type} JOIN {table} ON {on_condition}"
        self._query.joins.append(join_clause)
        return self

    def left_join(self, table, on_condition):
        """Convenience method for LEFT JOIN"""
        return self.join(table, on_condition, "LEFT")

    def where(self, condition):
        """Add a WHERE condition"""
        self._query.where_conditions.append(condition)
        return self

    def group_by(self, *columns):
        """Add GROUP BY columns"""
        self._query.group_by_columns.extend(columns)
        return self

    def having(self, condition):
        """Add a HAVING condition"""
        self._query.having_conditions.append(condition)
        return self

    def order_by(self, *columns):
        """Add ORDER BY columns"""
        self._query.order_by_columns.extend(columns)
        return self

    def limit(self, value):
        """Set LIMIT"""
        self._query.limit_value = value
        return self

    def offset(self, value):
        """Set OFFSET"""
        self._query.offset_value = value
        return self

    def build(self):
        """Return the constructed query"""
        return self._query