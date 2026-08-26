#!/bin/bash
cd public/learning/챕터2_완성동영상/

# Function to tone down and extract poster
process_video() {
  local input="$1"
  local base="$2"
  
  if [ -f "$input" ]; then
    echo "Processing $input -> $base.mp4"
    # Apply Option D Tone Down (sat=0.45, gamma=1.15)
    ffmpeg -y -i "$input" -vf "eq=saturation=0.45:gamma=1.15" -c:v libx264 -crf 18 -preset fast -movflags +faststart -an "tmp_$base.mp4" </dev/null
    mv "tmp_$base.mp4" "$base.mp4"
    
    # Extract Poster from END frame
    ffmpeg -y -sseof -0.5 -i "$base.mp4" -frames:v 1 -q:v 2 "$base-poster.jpg" </dev/null
  fi
}

process_video "scene-ch2-01.mp4" "scene-ch2-01"
process_video "Oak_tree_in_meadow_202608061427.mp4" "scene-ch2-02"
process_video "Giraffe_and_zebras_on_plain_202608061431.mp4" "scene-ch2-03"
process_video "Frog_leaps_from_mud_bank_202608061507.mp4" "scene-ch2-05"

# Clean up old files if they are not the new standard names
rm -f Oak_*.mp4 Giraffe_*.mp4 Frog_*.mp4
