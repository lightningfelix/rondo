{
   description = "flake";

   inputs = {
      nixpkgs.url = "https://channels.nixos.org/nixpkgs-unstable/nixexprs.tar.zst";
   };

   outputs = { self, nixpkgs, ... }: let
      pkgs = nixpkgs.legacyPackages."x86_64-linux";
   in {
      devShells.x86_64-linux.default = pkgs.mkShell {
	 packages = [
	    (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
	       pandas
	       anysqlite
	    ]))
	 ];
      };
   };
}
