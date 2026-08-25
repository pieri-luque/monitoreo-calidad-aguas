# config_ecas.py


ECA_AGUA = {
    "Subcategoría A1: Aguas superficiales destinadas a producción de agua potable (Desinfección simple)": {
        "pH": {"min": 6.5, "max": 8.5},
        "Conductividad Eléctrica (µS/cm)": {"max": 1500.0},
        "Oxígeno Disuelto (mg/L)": {"min": 6.0, "max": 14.0}, # Mínimo requerido para vida/calidad
        "Sólidos Suspendidos Totales (mg/L)": {"max": 25.0},
        "DBO5 (mg/L)": {"max": 3.0},
        "Aceites y Grasas (mg/L)": {"max": 0.5},
        "Plomo Total (mg/L)": {"max": 0.01},
        "Arsénico Total (mg/L)": {"max": 0.01},
        "Coliformes Termotolerantes (NMP/100mL)": {"max": 50.0}
    },
    "Subcategoría D1: Riego de vegetales (Cultivo de tallo bajo y alto)": {
        "pH": {"min": 6.5, "max": 8.5},
        "Conductividad Eléctrica (µS/cm)": {"max": 2500.0},
        "Oxígeno Disuelto (mg/L)": {"min": 4.0, "max": 14.0},
        "Sólidos Suspendidos Totales (mg/L)": {"max": 100.0}, # Valor referencial operativo
        "DBO5 (mg/L)": {"max": 15.0},
        "Aceites y Grasas (mg/L)": {"max": 5.0},
        "Plomo Total (mg/L)": {"max": 0.05},
        "Arsénico Total (mg/L)": {"max": 0.1},
        "Coliformes Termotolerantes (NMP/100mL)": {"max": 1000.0}
    },
    "ECA Aguas Residuales Domésticas y Municipales (LMP PTAR)": {
        "pH": {"min": 6.5, "max": 8.5},
        "Conductividad Eléctrica (µS/cm)": {"max": 5000.0}, # Límites operacionales PTAR mas amplios
        "Oxígeno Disuelto (mg/L)": {"min": 2.0, "max": 14.0},
        "Sólidos Suspendidos Totales (mg/L)": {"max": 150.0},
        "DBO5 (mg/L)": {"max": 100.0},
        "Aceites y Grasas (mg/L)": {"max": 20.0},
        "Plomo Total (mg/L)": {"max": 0.2},
        "Arsénico Total (mg/L)": {"max": 0.1},
        "Coliformes Termotolerantes (NMP/100mL)": {"max": 10000.0}
    }
}

# Diccionario de sinonimias exhaustivo enfocado en limpiar caracteres y hacer match exacto
# Diccionario simplificado compatible con el nuevo limpiador de app.py
SINONIMOS_PARAMETROS = {
    'ph': 'pH', 'phph': 'pH', 'p_h': 'pH',
    'conductividadelectricascm': 'Conductividad Eléctrica (µS/cm)', 
    'conductividadelectricauscm': 'Conductividad Eléctrica (µS/cm)',
    'conductividad': 'Conductividad Eléctrica (µS/cm)',
    'oxigenodisueltomgl': 'Oxígeno Disuelto (mg/L)', 'oxigeno': 'Oxígeno Disuelto (mg/L)', 'od': 'Oxígeno Disuelto (mg/L)',
    'solidossuspendidostotalesmgl': 'Sólidos Suspendidos Totales (mg/L)', 'sst': 'Sólidos Suspendidos Totales (mg/L)',
    'dbo5mgl': 'DBO5 (mg/L)', 'dbo5': 'DBO5 (mg/L)',
    'aceitesygrasasmgl': 'Aceites y Grasas (mg/L)', 'aceitesygrasas': 'Aceites y Grasas (mg/L)',
    'plomototalmgl': 'Plomo Total (mg/L)', 'pb': 'Plomo Total (mg/L)', 'plomo': 'Plomo Total (mg/L)',
    'arsenicototalmgl': 'Arsénico Total (mg/L)', 'as': 'Arsénico Total (mg/L)', 'arsenico': 'Arsénico Total (mg/L)',
    'colifórmestermotolerantesnmp100ml': 'Coliformes Termotolerantes (NMP/100mL)', 
    'colifermostermentables': 'Coliformes Termotolerantes (NMP/100mL)', 
    'coliformes': 'Coliformes Termotolerantes (NMP/100mL)',
    'colifermostermotolerantesnmp100ml': 'Coliformes Termotolerantes (NMP/100mL)'
}
