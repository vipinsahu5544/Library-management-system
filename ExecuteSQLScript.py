class ExecuteSQLScript:
    "This is class that contains the execute function which will execute all sql queries from sql_script.sql."
    def execute(self,filename,cursor):
        fb = open(filename,'r')
        sqlFile = fb.read()
        fb.close()
        sqlCommands = sqlFile.split(';')

        for command in sqlCommands:
            try:
                if command.strip()!= '':
                    cursor.execute(command)
            except IOError:
                print("command skipped:")



