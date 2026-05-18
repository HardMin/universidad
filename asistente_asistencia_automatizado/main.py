import pandas as pd


class asistencia_unesr:
    def __init__(self, df):
        self.excel = df
        self.data_new_excel = self.excel.copy()
        self.data_errors_excel = []

    def _veirificar_correo(self, email):
        if "@" in email and "." in email:
            return True
        else:
            return False

    def _verificar_datos_string(self, string):
        if isinstance(string, str) and len(string) > 0:
            return True
        else:
            return False

    def contar_asistencia(self, alumno):
        asistencia_column = alumno.filter(like="Asistencia_")

        resultado = (asistencia_column == "S").sum()

        dias = len(asistencia_column)

        estado = "Reprovado" if resultado / dias < 0.60 else "Aprobado"

        return dias, resultado, estado

    def asistencia(self, alumno):
        alumno_filtrado = self.excel.loc[alumno.Index]

        dias, resultado, estado = self.contar_asistencia(alumno_filtrado)

        self.data_new_excel["Total de dias"] = dias
        self.data_new_excel["Asistencia"] = resultado
        self.data_new_excel["Estado"] = estado

    def guardar_excel(self):
        df = pd.DataFrame(self.data_new_excel)
        df.to_excel("res_asistencia_unesr.xlsx", index=False, sheet_name="Asistencia")

    def start(self):
        for alumno in self.excel.itertuples():
            self.asistencia(alumno)

        self.guardar_excel()


if __name__ == "__main__":
    df = pd.read_excel("asistencia_unesr.xlsx")
    if not df.empty:
        asistencia = asistencia_unesr(df)
        asistencia.start()
    else:
        print("No hay datos en el archivo")
