class SQLQuery:
    """The product - represents a SQL query"""
    def __init__(self):
        self.select_columns = []
        self.from_table = None
        self.joins = []
        self.where_conditions = []
        self.group_by_columns = []
        self.having_conditions = []
        self.order_by_columns = []
        self.limit_value = None
        self.offset_value = None

    def to_sql(self):
        """Convert the query object to SQL string"""
        if not self.from_table:
            raise ValueError("FROM clause is required")

        # Build SELECT clause
        columns = ", ".join(self.select_columns) if self.select_columns else "*"
        sql = f"SELECT {columns}"

        # Add FROM clause
        sql += f"\nFROM {self.from_table}"

        # Add JOINs
        for join in self.joins:
            sql += f"\n{join}"

        # Add WHERE clause
        if self.where_conditions:
            conditions = " AND ".join(self.where_conditions)
            sql += f"\nWHERE {conditions}"

        # Add GROUP BY
        if self.group_by_columns:
            columns = ", ".join(self.group_by_columns)
            sql += f"\nGROUP BY {columns}"

        # Add HAVING
        if self.having_conditions:
            conditions = " AND ".join(self.having_conditions)
            sql += f"\nHAVING {conditions}"

        # Add ORDER BY
        if self.order_by_columns:
            columns = ", ".join(self.order_by_columns)
            sql += f"\nORDER BY {columns}"

        # Add LIMIT and OFFSET
        if self.limit_value:
            sql += f"\nLIMIT {self.limit_value}"
        if self.offset_value:
            sql += f"\nOFFSET {self.offset_value}"

        return sql