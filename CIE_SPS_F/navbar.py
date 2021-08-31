import dash_bootstrap_components as dbc

# Navigation Bar function
def Navbar():
    navbar = dbc.NavbarSimple(children=[
        
             dbc.NavItem(dbc.NavLink("Antecedentes", href='/antecedente')),
             dbc.NavItem(dbc.NavLink("Resultados", href='/res')),
             dbc.NavItem(dbc.NavLink("Banco de datos", href='/banco')),
             
        ],
        brand="Sistema de Percepción Social",
        brand_href="/",
        sticky="top",
        color= '#13322B',
        dark=True,
        expand='lg',)
    
    return navbar
