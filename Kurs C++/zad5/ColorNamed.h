# pragma once

# include <string>
# include "Color.h"

class ColorNamed : public virtual Color {
public:
    ColorNamed();

    ColorNamed(int r, int g, int b, std::string &name);

    std::string getName() const;

    void setName(std::string name);

private:
    std::string name;
};
