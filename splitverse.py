class splitverse():

    def split_debut(aled: str):
        split_debut = aled.split(" ")[0] + aled.replace("Python", " +")
        return split_debut

    def split_fin(aled: str):
        split_fin = aled.replace("language.", "+ ") + aled.split(" ")[-1]
        return split_fin

    def reverse(aled: str):
        reverse = aled[::-1]
        return reverse

    def reversed(aled: str):
        reversed = aled.split()[::-1]
        return reversed
