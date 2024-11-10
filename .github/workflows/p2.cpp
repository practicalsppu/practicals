#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<map>
#include<string>

using namespace std;

class MacroProcessor{
    public:
    vector <string> MNT;
    vector <string> MDT;
    vector <vector<string>> ALA;
    vector <string> IC;

    void processPass1(const string& sourceFileName)
    {
        ifstream sourceFile(sourceFileName);
        string line;
        bool inMacro = false;
        string currentMacro;
        vector <string> currentArguments;
        while(getline(sourceFile, line))
        {
            stringstream ss(line);
            string word;
            ss>>word;

            if (word == "MACRO")
            {
                inMacro = true;
                continue;
            }
            if(word == "MEND" && inMacro)
            {
                MNT.push_back(currentMacro);
                ALA.push_back(currentArguments);
                MDT.push_back("MACRO DEFINITION");
                for(auto& arg:currentArguments)
                {
                    MDT.push_back(arg);
                }
                currentArguments.clear();
                inMacro = false;
                continue;
            }
            if(inMacro)
            {
                MDT.push_back(line);
                continue;
            }
            IC.push_back(line);

        }
        sourceFile.close();
    }

    void printResults()
    {
        cout<<"MNT: "<<endl;
        for(const auto& entry : MNT)
        {
            cout<<entry<<endl;
        }
        cout<<"MDT: "<<endl;
        for(const auto& entry : MDT)
        {
            cout<<entry<<endl;
        }

        cout<<"ALA:"<<endl;
        for(const auto& args : ALA)
        {
            for(const auto& arg : args)
            {
                cout<<arg<<' ';
            }
            cout<<endl;
        }
        cout<<"Intermediate Code: "<<endl;
        for(const auto& code : IC)
        {
            cout<<code<<endl;
        }
    }
};

int main()
{
    MacroProcessor processor;
    string sourceFile = "source.asm";
    processor.processPass1(sourceFile);
    processor.printResults();
    return 0;
}