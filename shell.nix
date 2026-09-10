let
   pkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/nixpkgs-26.05-darwin.tar.gz") {};
in pkgs.mkShell {
   packages = [
      (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
	 pandas
	 anysqlite
      ]))
   ];
}
