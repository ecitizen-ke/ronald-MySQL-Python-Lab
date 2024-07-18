from app.db import Connection


class State:
    states =[]
    capitals = []
    admitedBtw1750and1850 = []
    state_capital = []
    def __init__(self):
        self.db = Connection()

    def get_States(self):
        """select all records from table states"""
        query = "SELECT * FROM states"
        self.db.cursor.execute(query)

        # Retrieve the user record in the database: returns a tuple
        data = self.db.cursor.fetchall()
        if data:
            for row in data:
                state ={
                    'id': row[0],
                    'name': row[1],
                    'abbreviation': row[2],
                    'capital': row[3],
                    'population': row[4],
                    'year_admitted': row[5]
                }
                self.states.append(state)
            return self.states
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()
        
    def create(self, name, abbreviation,capital, population,  year_admitted):
        """
         inserts a new state into the `states` table in the database
        """
        self.name = name
        self.abbreviation = abbreviation
        self.capital = capital
        self.population = population
        self.year_admitted = year_admitted

        # User data
        state = (self.name, self.abbreviation, self.capital, self.population, self.year_admitted)
        
        check_query =  "SELECT * FROM states WHERE name=%s AND abbreviation=%s"
        self.db.cursor.execute(check_query,[self.name, self.abbreviation])
        specific_record= self.db.cursor.fetchone()
        
        if specific_record:
            print("State already exists in the database.")
            return False
        # our values will be represented here by placeholders
        query = "INSERT INTO states ( name, abbreviation,capital, population,  year_admitted) VALUES(%s, %s, %s, %s, %s)" 

        # Execute query that inserts user data into the database
        record= self.db.cursor.execute(query, state)
        # check if query execution is successful
        result=self.db.cursor.rowcount
             # Commit data to the database
        if result:
             self.db.conn.commit()     
             
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()
        
        return record
    
    def list_states_starting_with_A(self):
        """List all records from table states where name starts with 'A'"""
        query = "SELECT * FROM states WHERE name LIKE 'A%'"
        self.db.cursor.execute(query)
        data= self.db.cursor.fetchall()
        if data:
            for row in data:
                state ={}
         
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()
        return data  
    
    
    def filter_states_by_name_asc(self):
        query = "SELECT * FROM states ORDER BY name ASC "
        self.db.cursor.execute(query)
        data= self.db.cursor.fetchall()
        for row in data:
            print(row)
          
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()
        return data 
        
    def update_states_population(self, id, population):
        """Update the states population"""
        self.id = id
        self.population = population
        # user data
        state = (self.population, self.id)
        update_query = "UPDATE states SET population = %s WHERE id = %s"      
       
        self.db.cursor.execute(update_query, state)
        result = self.db.cursor.rowcount
              # Commit data to the database
        if result:
            self.db.conn.commit()
            return "State population updated successfully."
          
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()
        
    def delete_state(self, id):
        """Delete a state record"""
        self.id = id
        delete_query = "DELETE FROM states WHERE id = %s"
        self.db.cursor.execute(delete_query, [self.id])
        result = self.db.cursor.rowcount
        
        # Commit data to the database
        if result:
            self.db.conn.commit()
            return "State deleted successfully."
        
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()   
         
    def get_highest_populated_state(self):
        """
        finds the most populous state in the database
        """
        query = "SELECT * FROM states WHERE population =(SELECT MAX(population))"
        self.db.cursor.execute(query)
        data= self.db.cursor.fetchone()
        if data:
            return data
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()
        
    def search_states(self,name):
        """ search for a state by name in the database """
        query = "SELECT * FROM states WHERE name = %s"
        self.db.cursor.execute(query, [name])
        data= self.db.cursor.fetchone()
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()
        return data
    def list_state_capitals(self):
        """
        lists all state capitals from the database
        """
        query = "SELECT capital FROM states"
        self.db.cursor.execute(query)
        data= self.db.cursor.fetchall()
        if data:
             for row in data:
                 capital ={
                'capital': row[0]
                 }
                 self.capitals.append(capital)
             return self.capitals
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()
        return data 
    def average_population(self):
        """
        calculates the average population of states in the database
        """
        query = "SELECT AVG(population) FROM states"
        self.db.cursor.execute(query)
        average_population = self.db.cursor.fetchone()  
       
        #close the cursor
        self.db.cursor.close()
        # close the connection
        self.db.conn.close()
        
        return average_population
        
    def count_population_range(self):
        """
        this founction counts number of the states with a population range between 1000000 and 5000000
        """
        query = "SELECT population FROM states WHERE population BETWEEN 1000000 AND 5000000"
        self.db.cursor.execute(query)
        data= self.db.cursor.fetchall()
       
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()    
        return len(data)
    
    def join_states_capital(self):
      
        """
        this function joins t joins the `states` and `capitals` tables to display state names along with their capitals
        """
        query="SELECT states.name, capitals.capital_name FROM states INNER JOIN capitals ON states.id=capitals.state_id ORDER BY states.id ASC"
        
        self.db.cursor.execute(query)
        rows = self.db.cursor.fetchall()
        print(rows)
        if rows:
            for row in rows:
                state = {
                    'name': row[0],
                    'capital': row[1]
                }
                self.state_capital.append(state)
            return self.state_capital
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close() 
     
    def search_State_By_Name(self,name):
        """
        this functions searches for state details by name
        """
        query="SELECT * FROM states WHERE name=%s"

        self.db.cursor.execute(query,[name])

        result=self.db.cursor.fetchall()
        for row in result:
            print(row)

        #Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()

        return result    
        
    def    state_admitted_btw_1750_AND_1850(self):
        """
        this function returns all states that were admitted between 1750 and 1850
        """
        query="SELECT * FROM states WHERE year_admitted BETWEEN 1750 AND 1850"
        
        self.db.cursor.execute(query)
        result=self.db.cursor.fetchall()
        if result:
            for row in result:
                admitedBtw = {
                    'id': row[0],
                    'name': row[1],
                    'abbreviation': row[2],
                    'capital': row[3],
                    'population': row[4],
                    'year_admitted': row[5]
                }
                self.admitedBtw1750and1850.append(admitedBtw)
            return self.admitedBtw1750and1850      
        #Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()
        return result
          