#include<string>

class Duree
{
public:
  Duree(int heure, int minute, int seconde):
    m_heure(heure), m_minute(minute), m_seconde(seconde){};
  Duree operator+=(const Duree &  duree);
  std::string affiche();
  int dureeToSeconds() const;

private:
  int m_heure;
  int m_minute;
  int m_seconde;
  int intoSeconds();

};

Duree operator-(const Duree & duree1, const Duree & duree2);

bool operator<(const Duree & duree1, const Duree & duree2);
Duree secondsToDuree( const int p_seconds);
