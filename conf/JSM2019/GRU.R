#Code taken/modified from Deep Learning with R, by Francois Chollet & Joseph J. Allaire examples, and subject to:

#The MIT License (MIT)

#Copyright © 2017 Francois Chollet
#Copyright © 2017 J.J. Allaire

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files 
#(the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, 
#publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do 
#so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

library(keras)

max_features <- 10000
maxlen <- 500
batch_size <- 32

imdb <- dataset_imdb(num_words = max_features)
c(c(input_train, y_train), c(input_test, y_test)) %<-% imdb 
cat(length(input_train), "train sequences\n")
cat(length(input_test), "test sequences")

input_train <- pad_sequences(input_train, maxlen = maxlen)
input_test <- pad_sequences(input_test, maxlen = maxlen)
cat("input_train shape:", dim(input_train), "\n")
cat("input_test shape:", dim(input_test), "\n")


model <- keras_model_sequential() %>% 
  layer_embedding(input_dim = max_features, output_dim = 32) %>% 
  layer_gru(units = 32) %>% 
  layer_dense(units = 1, activation = "sigmoid")

model %>% compile(
  optimizer = "rmsprop",
  loss = "binary_crossentropy",
  metrics = c("acc")
)

history <- model %>% fit(
  input_train, y_train,
  epochs = 10,
  batch_size = 128,
  validation_split = 0.2
)

summary(model)

history$metrics