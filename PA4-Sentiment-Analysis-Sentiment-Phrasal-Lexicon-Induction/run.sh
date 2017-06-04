for entry in "/home/jigna/Downloads/data/pos/"*
do
   ./tagchunk.i686 -predict . w-5 "/home/jigna/Downloads/data/pos/${entry##*/}" resources > data/output/pos/"${entry##*/}"
done

for entry in "/home/jigna/Downloads/data/neg/"*
do
   ./tagchunk.i686 -predict . w-5 "/home/jigna/Downloads/data/neg/${entry##*/}" resources > data/output/neg/"${entry##*/}"
done
