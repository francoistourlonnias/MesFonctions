#ifndef FELIN_H_INCLUDED
#define FELIN_H_INCLUDED

#include <iostream>

class Felin
{
    protected :
        std::string m_nom, m_espece;
        int m_age;

    public :
        Felin(std::string nom, std::string espece, int age);
        std::string seNourrir();
        std::string sePresenter();

};

#endif // FELIN_H_INCLUDED
