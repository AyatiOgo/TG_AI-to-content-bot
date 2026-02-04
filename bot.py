import os
import logging 
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler
from generate import generate_blog_post, generate_short_form, generate_x_posts, generate_linkedin_posts, parse_blog_content, save_blog_to_docx
# from transcribe import transcribe
from transcribe_v2 import transcribe
import tempfile

load_dotenv()

# LOGGING SYSTEM
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)



async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
            await update.message.reply_text(
                    "👋 Hi! I'm your Video-to-Content bot.\n\n"
                    "Send me a video and I will:\n"
                    "1️⃣ Transcribe it\n"
                    "2️⃣ Ask you what you want\n\n"
                    "Then choose:\n"
                    "📱 /short — Convert to 3 short-form social media posts\n"
                    "📝 /blog  — Convert to a long-form blog post\n\n"
                    "Go ahead and send a video!"
            )


async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📥 Received your video! Downloading...")

    if update.message.video:
        video_file = update.message.video
    elif update.message.document and update.message.document.mime_type.startswith("video/"):
        video_file = update.message.document
    else:
        await update.message.reply_text("❌ I only accept video files. Please send a video!")
        return

    # Download the video to a temporary location
    file = await context.bot.get_file(video_file.file_id)
    original_name = video_file.file_name or "video.mp4"
    ext = os.path.splitext(original_name)[1]  # Gets .mp4, .mov, .avi, etc.

    video_path = os.path.join(tempfile.gettempdir(), f"video_{update.effective_user.id}{ext}")

    await file.download_to_drive(video_path)

    print(f"📁 Saved video to: {video_path}")
    print(f"📁 File exists: {os.path.exists(video_path)}")
    print(f"📁 File size: {os.path.getsize(video_path) if os.path.exists(video_path) else 'N/A'}")

    await update.message.reply_text("🎙️ Transcribing your video... (this may take a minute)")

    # Transcribe the video
    try:
        transcript = transcribe(video_path)
    except Exception as e:
        logger.error(f"Transcription failed: {e}")
        await update.message.reply_text("❌ Transcription failed. Please try again with a different video.")
        return

    # Clean up the video file
    if os.path.exists(video_path):
        os.remove(video_path)

    # Store transcript in user_data so /short and /blog can access it
    context.user_data["transcript"] = transcript

    await update.message.reply_text(
        "✅ Transcription complete!\n\n"
        "Now choose what you want:\n"
        "📱 /short — 3 short-form social media posts\n"
        "🐤 /X_Post — 3 structured X posts\n"
        "💼 /Linkedin_Post — 2 linkedin-form social media posts\n"
        "📝 /blog  — A long-form blog post"
    )


async def create_short(update: Update, context: ContextTypes.DEFAULT_TYPE):
    transcript = context.user_data.get("transcript")

    if not transcript:
        await update.message.reply_text("❌ No transcript found. Please send a video first!")
        return

    await update.message.reply_text("✨ Generating short-form content...")

    try:
        short_content = generate_short_form(transcript)
    except Exception as e:
        logger.error(f"Content generation failed: {e}")
        await update.message.reply_text("❌ Something went wrong. Please try again.")
        return

    await update.message.reply_text(
        f"📱 Here are your 3 short-form posts:\n\n{short_content}"
    )


async def create_x_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    transcript = context.user_data.get("transcript")

    if not transcript:
        await update.message.reply_text("❌ No transcript found. Please send a video first!")
        return

    await update.message.reply_text("✨ Generating x-post content...")

    try:
        short_content = generate_x_posts(transcript)
    except Exception as e:
        logger.error(f"Content generation failed: {e}")
        await update.message.reply_text("❌ Something went wrong. Please try again.")
        return

    await update.message.reply_text(
        f"📱 Here are your 3 x-content posts:\n\n{short_content}"
    )

async def create_linkedin_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    transcript = context.user_data.get("transcript")

    if not transcript:
        await update.message.reply_text("❌ No transcript found. Please send a video first!")
        return

    await update.message.reply_text("✨ Generating linkedin-form content...")

    try:
        short_content = generate_linkedin_posts(transcript)
    except Exception as e:
        logger.error(f"Content generation failed: {e}")
        await update.message.reply_text("❌ Something went wrong. Please try again.")
        return

    await update.message.reply_text(
        f"📱 Here are your 2 linkedin-form posts:\n\n{short_content}"
    )

async def create_blog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    transcript = context.user_data.get("transcript")

    if not transcript:
        await update.message.reply_text("❌ No transcript found. Please send a video first!")
        return

    await update.message.reply_text("✨ Generating your blog post...")

    try:
        blog_post = generate_blog_post(transcript)
        file_path = save_blog_to_docx(blog_post)
    except Exception as e:
        logger.error(f"Blog generation failed: {e}")
        await update.message.reply_text("❌ Something went wrong. Please try again.")
        return

    # Send document instead of long text
    with open(file_path, "rb") as doc_file:
        await update.message.reply_document(
            document=doc_file,
            filename="Your_Blog_Post.docx",
            caption="📝 Here is your generated blog post!"
        )

    # Optional: clean up temp file
    os.remove(file_path)

def main():
        token = os.getenv('BOT_TOKEN')
        if not token:
                raise ValueError('Telegram Bot Token is Not set')
        app = Application.builder().token(token).build()

        app.add_handler(CommandHandler('start', start))
        app.add_handler(CommandHandler('short', create_short))
        app.add_handler(CommandHandler('blog', create_blog))
        app.add_handler(CommandHandler('X_Post', create_x_post))
        app.add_handler(CommandHandler('Linkedin_Post', create_linkedin_post))

        # Handle Video Message
        app.add_handler(
        MessageHandler(
            filters.VIDEO or filters.Document() ,
            handle_video
        )
    )
        print("🤖 Bot is running... (Press Ctrl+C to stop)")
        app.run_polling()

if __name__ == "__main__":
    main()