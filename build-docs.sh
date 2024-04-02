set -e

quarto add --no-prompt machow/quartodoc && \
python -m quartodoc build --verbose && \
python -m quartodoc interlinks && \
quarto render
