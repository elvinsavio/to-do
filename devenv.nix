{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/basics/
  env.VENV = ".venv";

  # https://devenv.sh/packages/
  packages = with pkgs; [ 
	pkgs.git
	pkgs.vscodium
	pkgs.python312
	pkgs.python312Packages.pip	
	pkgs.python312Packages.virtualenv	 
        nodejs_21
];

  # https://devenv.sh/scripts/
  scripts.install.exec = ''
    if [ ! -p "$VIRTUAL_ENV" ]; then
      echo "in venv"
    fi
  
    '';


  enterShell = ''
    git config user.name "elvinsavio"
    git config user.email "elvinsavio.lp@gmail.com"

    if [ ! -p "$VENV" ]; then
      python3 -m venv $VENV
    fi

    source $VENV/bin/activate
  '';

  # https://devenv.sh/tests/
  enterTest = ''
    echo "Running tests"
    git --version | grep "2.42.0"
  '';

  # https://devenv.sh/services/
  # services.postgres.enable = true;

  # https://devenv.sh/languages/
  # languages.nix.enable = true;

  # https://devenv.sh/pre-commit-hooks/
  # pre-commit.hooks.shellcheck.enable = true;

  # https://devenv.sh/processes/
  # processes.tailwind.exec = "npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch";

  # See full reference at https://devenv.sh/reference/options/
}
